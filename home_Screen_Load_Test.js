// import http from 'k6/http';
// import { check } from 'k6';

// export const options = {
//     vus: 10,
//     duration: '10s',
// };

// export default function () {
//     // URLs for the requests
//     const url1 = "https://stage-api.getstan.app/api/v3/user/onboarding/status";
//     const url2 = "https://stage-api.getstan.app/api/v1/users/profile/percentage";
//     const url3 = "https://stage-api.getstan.app/api/v3/users/gamecurrency";
//     const url4 = "https://stage-api.getstan.app/api/v1/user/offers/stats";
//     const url5 = "https://stage-api.getstan.app/api/v3/user/coins"
//     const url6 = "https://stage-api.getstan.app/api/v3/app/carousels/home"
//     const url7 = "https://stage-api.getstan.app/api/v3/user/rewards/status"
//     const url8 = "https://stage-api.getstan.app/api/v4/home/games" 
//     const url9 = "https://stage-api.getstan.app/api/v3/user/carousels/levelup"
//     const url10 = "https://stage-api.getstan.app/api/v4/fetch/streak/status" 
//     const url11 = "https://stage-api.getstan.app/api/v2/app/championships"
//     const url12 = "https://stage-api.getstan.app/api/v4/home/marketwatch-and-winners" 
//     const url13 = "https://stage-api.getstan.app/api/v1/articles/suggested"
//     const url14 = "https://stage-api.getstan.app/api/v1/user/inapp/messages"
//     const url15 = "https://stage-api.getstan.app/engagement/api/v1/events"
//     const url16 = "https://stage-api.getstan.app/api/v2/users/missions/info"
//     const url17 = "https://stage-api.getstan.app/api/v1/agora/channels"
//     const url18 = "https://stage-api.getstan.app/api/v1/users/update-profile"
//      // New URL for the club gifts endpoint
//      // New URL for the club gifts endpoint
    
//     // Common headers for all requests
//     const params = {
//         headers: {
//             "Accept": "application/json, text/plain, */*",
//             "gaid": "9af1c2ff-4a28-4032-ae0c-b256b9258fe8",
//             "AppVersion": "102",
//             "Platform": "android",
//             "SID": "1707129850016-19612",
//             "TS": "undefined", // Consider addressing the "undefined" value
//             "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJiZ21pUHJvZmlsZUlkIjo5MzMzLCJleHAiOjE3MDcyMTQyMzMsImZyZWVmaXJlUHJvZmlsZUlkIjo5MzMwLCJpYXQiOjE3MDcxMjc4MzMsImlkIjo3MTE3fQ.RITXwoWuUc49hkcUYWmJL1xslhgL5s2FJrQHs4npf04"
//         }
//     };

//     // Making the requests
//     let response1 = http.get(url1, params);
//     let response2 = http.get(url2, params);
//     let response3 = http.get(url3, params); // New request for club gifts

//     // Checks for the first and second requests are unchanged
//     check(response1, {
//         'API /user/join status is 200': (r) => r.status === 200,
//         'API /user/join body is not empty': (r) => r.body.length > 0,
//     });

//     check(response2, {
//         'API /channels status is 200': (r) => r.status === 200,
//         'API /channels body is not empty': (r) => r.body.length > 0,
//     });

//     // Checks for the new request
//     check(response3, {
//         'API /club-gifts status is 200': (r) => r.status === 200,
//         'API /club-gifts body is not empty': (r) => r.body.length > 0,
//     });

import http from 'k6/http';
import { check } from 'k6';

export const options = {
    vus: 5,
    duration: '10s',
};

export default function () {
    const urls = [
        "https://stage-api.getstan.app/api/v3/user/onboarding/status",
        "https://stage-api.getstan.app/api/v1/users/profile/percentage",
        "https://stage-api.getstan.app/api/v3/user/gamecurrency",
        "https://stage-api.getstan.app/api/v1/user/offers/stats",
        "https://stage-api.getstan.app/api/v3/user/coins",
        "https://stage-api.getstan.app/api/v3/app/carousels/home",
        "https://stage-api.getstan.app/api/v3/user/rewards/status",
        "https://stage-api.getstan.app/api/v4/home/games", 
        "https://stage-api.getstan.app/api/v3/user/carousels/levelup",
        "https://stage-api.getstan.app/api/v4/fetch/streak/status", 
        "https://stage-api.getstan.app/api/v2/app/championships",
        "https://stage-api.getstan.app/api/v4/home/marketwatch-and-winners", 
        "https://stage-api.getstan.app/api/v1/articles/suggested",
        "https://stage-api.getstan.app/api/v1/user/inapp/messages",
        "https://stage-api.getstan.app/engagement/api/v1/events",
        "https://stage-api.getstan.app/api/v2/users/missions/info",
        "https://stage-api.getstan.app/api/v1/agora/channels",
        "https://stage-api.getstan.app/api/v1/users/update-profile"
        
    ];

    const params = {
        headers: {
            "Accept": "application/json, text/plain, */*",
            "gaid": "9af1c2ff-4a28-4032-ae0c-b256b9258fe8",
            "AppVersion": "102",
            "Platform": "android",
            "SID": "1707129850016-19612",
            "TS": "some_value", // Previously "undefined", you should provide a meaningful value or remove if not needed
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJiZ21pUHJvZmlsZUlkIjo5MzMzLCJleHAiOjE3MDcyMTQyMzMsImZyZWVmaXJlUHJvZmlsZUlkIjo5MzMwLCJpYXQiOjE3MDcxMjc4MzMsImlkIjo3MTE3fQ.RITXwoWuUc49hkcUYWmJL1xslhgL5s2FJrQHs4npf04"
        }
    };

    const putPayload = {
        "firebaseToken": "deNn_kL9RGKLg5STs0mgin:APA91bHYcAuV_KiTtYjWs2iKvYZuuwe3MpVc2A5tXoMDqxabgT-qlFlB18bL2B4Ja5zAWAASfEnACcmBM2mFCXJl9VNCoMfRCxAQ8sKRbh8kW_XRaJ9Rw33ATPe1_uqbb39kpy4c4dut"
    };
    
    urls.forEach(url => {
        let response;

        if (url.includes("users/update-profile")) {
            // Use a PUT request for users/update-profile
            response = http.put(url, putPayload, params);
        } else {
            // Use a GET request for all other URLs
            response = http.get(url, params);
        }

        // Log the URL and response status
        console.log(`URL: ${url} - Status: ${response.status}`);

        // Optionally, log a snippet of the response body
        console.log(`Response body snippet for ${url}: ${response.body.slice(0, 100)}...`);

        // Perform checks on the response
        check(response, {
            [`Status is 200 for ${url}`]: (r) => r.status === 200,
            [`Body is not empty for ${url}`]: (r) => r.body.length > 0,
        });
    });
}