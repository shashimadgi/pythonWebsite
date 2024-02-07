import http from 'k6/http';
import { check } from 'k6';

export const options = {
    vus: 50,
    duration: '10s',
    thresholds: {
        checks: ['rate==1.00'], // Ensure 100% of checks must pass
    },
};

export default function () {
    const urls = [
        "https://api.getstan.app/api/v3/user/onboarding/status",
        "https://api.getstan.app/api/v1/users/profile/percentage",
        "https://api.getstan.app/api/v3/user/gamecurrency",
        "https://api.getstan.app/api/v1/user/offers/stats",
        "https://api.getstan.app/api/v3/user/coins",
        "https://api.getstan.app/api/v3/app/carousels/home",
        "https://api.getstan.app/api/v3/user/rewards/status",
        "https://api.getstan.app/api/v4/home/games", 
        "https://api.getstan.app/api/v3/user/carousels/levelup",
        "https://api.getstan.app/api/v4/fetch/streak/status", 
        "https://api.getstan.app/api/v2/app/championships",
        "https://api.getstan.app/api/v4/home/marketwatch-and-winners", 
        "https://api.getstan.app/api/v1/articles/suggested",
        "https://api.getstan.app/api/v1/user/inapp/messages",
        "https://api.getstan.app/engagement/api/v1/events",
        "https://api.getstan.app/api/v2/users/missions/info",
        "https://api.getstan.app/api/v1/agora/channels",
        "https://api.getstan.app/api/v1/users/update-profile"
        
    ];

    const params = {
        headers: {
            "Accept": "application/json, text/plain, */*",
            "gaid": "9af1c2ff-4a28-4032-ae0c-b256b9258fe8",
            "AppVersion": "108",
            "Platform": "android",
            "GameId": "freefire",
            "SID": "1707129850016-19612",
            "TS": "some_value", // Previously "undefined", you should provide a meaningful value or remove if not needed
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJiZ21pUHJvZmlsZUlkIjo0Mzc5MjksImV4cCI6MTcwOTg4MjI4MSwiZnJlZWZpcmVQcm9maWxlSWQiOjQzNzkzOCwiaWF0IjoxNzA3MjkwMjgxLCJpZCI6NTA5NjIxfQ.A-RN9ieipztLIdcC6R-mOLnySHV9gozRdIC8EAmZFjs"
        }
    };

    const putPayload = {
        
            "username" : "Y0Z1OZAN",
            "name": "Opgamer",
            "bio": "Ghhfhgjghugugy ghgjhfhhhdjjjh gyvycycctxtxtxtctctxtxtuvuhdhd"
        
    };
    
    urls.forEach(url => {
        let response;

        if (url.includes("users/update-profile")) {
            response = http.put(url, JSON.stringify(putPayload), params);
        } else {
            response = http.get(url, params);
        }

        const isStatus200 = response.status === 200;
        const isBodyNotEmpty = response.body ? response.body.length > 0 : false;

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
