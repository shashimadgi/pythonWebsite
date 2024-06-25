
import { htmlReport } from "https://raw.githubusercontent.com/benc-uk/k6-reporter/main/dist/bundle.js";
import { textSummary } from "https://jslib.k6.io/k6-summary/0.0.1/index.js";

import http from 'k6/http';
import { check } from 'k6';


export function handleSummary(data) {
    return {
      "results.html": htmlReport(data),
      stdout: textSummary(data, { indent: " ", enableColors: true }),
    };
  }
 
export const options = {
    vus: 5,
    duration: '5s',
    thresholds: {
        checks: ['rate==1.00'], // Ensure 100% of checks must pass
    },
};


export default function () {
    // Define request headers from original fetch API example
    let headers = {
        "Accept": "application/json, text/plain, */*",
        "gaid": "e3e92938-0b86-4ac5-9270-08e85ee30b0c",
        "AppVersion": "120",
        "Platform": "android",
        "SID": "1719303489596-28317",
        "TS": "undefined",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJiZ21pUHJvZmlsZUlkIjo0Mzc5MjksImV4cCI6MTcyMTkwNDk5NiwiZnJlZWZpcmVQcm9maWxlSWQiOjQzNzkzOCwiaWF0IjoxNzE5MzEyOTk2LCJpZCI6NTA5NjIxfQ.DxcMp5LBmeNsiedWn3_eDMWR4rYlSzwmS04HFbEP55w"
    };

   
    let response1 = http.get("https://api.getstan.app/api/v5/get/live-clubs?limit=10&offset=0", { headers: headers });

   
    check(response1, {
        'status is 200': r => r.status === 200,
        'API /channels body is not empty': (r) => r.body.length > 0,

    });
    let response2 = http.get("https://api.getstan.app/api/v5/get/upcoming-clubs?limit=10&offset=0", { headers: headers });

    

    check(response2, {
        "is status 200": (r) => r.status === 200,
        "body is not empty": (r) => r.body.length > 0
    });
    console.log('Response received: ' + response2.body);


    // let ur3 = 'https://api.getstan.app/api/v5/club/messages?clubId=AGPCIUE7';
    let response3 = http.get("https://api.getstan.app/api/v5/club/messages", { headers: headers });
    check(response3, {
        "is  club/messages? status 200": (r) => r.status === 200,
        " club/messages? body  is not empty": (r) => r.body.length > 0
    });

    console.log('Response received: ' + response3.body);

    let response4 = http.get("https://api.getstan.app/api/v4/club-pass/balance", { headers: headers });
    check(response4, {
        "is  club-pass/balance status 200": (r) => r.status === 200,
        " club-pass/balance body  is not empty": (r) => r.body.length > 0
    });

    console.log('Response received: ' + response4.body);

    let response5 = http.get("https://api.getstan.app/api/v4/club-gift/fetch-inventory", { headers: headers });
    check(response5, {
        "is  club-gift/fetch-inventory status 200": (r) => r.status === 200,
        " club-gift/fetch-inventory body  is not empty": (r) => r.body.length > 0
    });

    console.log('Response received: ' + response5.body);

    let response6 = http.get("https://api.getstan.app/api/v1/agora/club-gifts", { headers: headers });
    check(response6, {
        "is  agora/club-gifts status 200": (r) => r.status === 200,
        " agora/club-gifts body  is not empty": (r) => r.body.length > 0
    });

    console.log('Response received: ' + response6.body);

    let response7 = http.get("https://api.getstan.app/api/v4/club-pass/getSKU", { headers: headers });
    check(response7, {
        "is  club-pass/getSKU status 200": (r) => r.status === 200,
        " club-pass/getSKU body  is not empty": (r) => r.body.length > 0
    });

    console.log('Response received: ' + response7.body);

    let response8 = http.get("https://api.getstan.app/api/v5/clubs/rewards", { headers: headers });
    check(response8, {
        "is  clubs/rewards status 200": (r) => r.status === 200,
        " clubs/rewards body  is not empty": (r) => r.body.length > 0
    });

    console.log('Response received: ' + response8.body);

    let response9 = http.get("https://api.getstan.app/api/v5/clubs/rewards/past", { headers: headers });
    check(response9, {
        "is  clubs/rewards/paststatus 200": (r) => r.status === 200,
        " clubs/rewards/past body  is not empty": (r) => r.body.length > 0
    });

    console.log('Response received: ' + response9.body);
    let response10 = http.get("https://api.getstan.app/api/v5/user/club", { headers: headers });
    check(response10, {
        "is  user/club status 200": (r) => r.status === 200,
        " user/club body  is not empty": (r) => r.body.length > 0
    });

    console.log('Response received: ' + response10.body);

    console.log('Response received: ' + response9.body);
    let response11 = http.get("https://api.getstan.app/api/v5/club/categories", { headers: headers });
    check(response11, {
        "is  club/categories status 200": (r) => r.status === 200,
        " club/categories body  is not empty": (r) => r.body.length > 0
    });

    console.log('Response received: ' + response11.body);



    // console.log(`Response time for live-clubs endpoint: ${response.timings.duration} ms`);
}
