
import http from 'k6/http';
import { check } from 'k6';

export const options = {
    vus: 5,
    duration: '10s',
    thresholds: {
        checks: ['rate==1.00'], // Ensure 100% of checks must pass
    },
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
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJiZ21pUHJvZmlsZUlkIjo5MzMzLCJleHAiOjE3MDczMDA5NzUsImZyZWVmaXJlUHJvZmlsZUlkIjo5MzMwLCJpYXQiOjE3MDcyMTQ1NzUsImlkIjo3MTE3fQ.w6hCMxZgpCUN1xtUwOGY-zRPyiV_2GMj_uKZxPL7PxI"
        }
    };

    const putPayload = {
        "firebaseToken": "deNn_kL9RGKLg5STs0mgin:APA91bHYcAuV_KiTtYjWs2iKvYZuuwe3MpVc2A5tXoMDqxabgT-qlFlB18bL2B4Ja5zAWAASfEnACcmBM2mFCXJl9VNCoMfRCxAQ8sKRbh8kW_XRaJ9Rw33ATPe1_uqbb39kpy4c4dut"
    };
    
    urls.forEach(url => {
        let response;

        if (url.includes("users/update-profile")) {
            response = http.put(url, JSON.stringify(putPayload), params);
        } else {
            response = http.get(url, params);
        }

        const isStatus200 = response.status === 200;
        const isBodyNotEmpty = response.body.length > 0;

        const checkResult = check(response, {
            [`Status is 200 for ${url}`]: (r) => isStatus200,
            [`Body is not empty for ${url}`]: (r) => isBodyNotEmpty,
        });

        // Log the URL and status if the check fails
        if (!checkResult) {
            console.error(`Check failed for ${url} - Status: ${response.status}`);
        }
    });
}
