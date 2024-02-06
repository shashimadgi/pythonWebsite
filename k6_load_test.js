import http from 'k6/http';
import { check } from 'k6';

export const options = {
    vus: 10,
    duration: '10s',
};

export default function () {
    // URLs for the requests
    const url1 = "https://stage-api.getstan.app/api/v1/agora/user/join?channel=D6R8KYHG";
    const url2 = "https://stage-api.getstan.app/api/v1/agora/channels?offset=0&pageSize=30&lastId=-1";
    const url3 = "https://stage-api.getstan.app/api/v1/agora/club-gifts?channel=D6R8KYHG"; // New URL for the club gifts endpoint
    
    // Common headers for all requests
    const params = {
        headers: {
            "Accept": "application/json, text/plain, */*",
            "gaid": "9af1c2ff-4a28-4032-ae0c-b256b9258fe8",
            "AppVersion": "102",
            "Platform": "android",
            "SID": "1707129850016-19612",
            "TS": "undefined", // Consider addressing the "undefined" value
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJiZ21pUHJvZmlsZUlkIjo5MzMzLCJleHAiOjE3MDcyMTQyMzMsImZyZWVmaXJlUHJvZmlsZUlkIjo5MzMwLCJpYXQiOjE3MDcxMjc4MzMsImlkIjo3MTE3fQ.RITXwoWuUc49hkcUYWmJL1xslhgL5s2FJrQHs4npf04"
        }
    };

    // Making the requests
    let response1 = http.get(url1, params);
    let response2 = http.get(url2, params);
    let response3 = http.get(url3, params); // New request for club gifts

    // Checks for the first and second requests are unchanged
    check(response1, {
        'API /user/join status is 200': (r) => r.status === 200,
        'API /user/join body is not empty': (r) => r.body.length > 0,
    });

    check(response2, {
        'API /channels status is 200': (r) => r.status === 200,
        'API /channels body is not empty': (r) => r.body.length > 0,
    });

    // Checks for the new request
    check(response3, {
        'API /club-gifts status is 200': (r) => r.status === 200,
        'API /club-gifts body is not empty': (r) => r.body.length > 0,
    });

    // Logging responses
    // console.log('Response from /user/join:', response1.body);
    // console.log('Response from /channels:', response2.body);
    // console.log('Response from /club-gifts:', response3.body); // Log the new response
}




// import http from 'k6/http';
// import { check, sleep } from 'k6';

// export const options = {
//     vus: 10,
//     duration: '10s',
//     // stages: [
//     //     { duration: '10s', target: 30 },
//     //     { duration: '10s', target: 50 },
//     //     { duration: '20s', target: 5 },
//     //   ],
// };

// const BASE_URL = 'https://stage-api.getstan.app'; // Define BASE_URL

// const generatePhoneNumber = () => {
//     let number = Math.floor(10 ** 8 + Math.random() * (9 * (10 ** 8)));
//     return '+919' + number;
// };

// export default function () {
//   const headers = {
//     "Accept": "application/json, text/plain, */*",
//     "Content-Type": "application/json",
//     "GameId": "bgmi",
//     "AppVersion": "94",
//     "Platform": "android",
//     "SID": "1689061440422-74140",
//     "TS": "877888888888"
//   };
  
//   const phone = generatePhoneNumber(); // Correctly declare phone a single time
//   console.log("======USER PHONE======", phone);
  
//   // Send OTP
//   const sendOtpResponse = http.post(`${BASE_URL}/api/v1/auth/otp/send`, JSON.stringify({ phone }), { headers });
//   check(sendOtpResponse, { 'OTP sent successfully.': (resp) => resp.status === 200 });
//   sleep(1); // Adjust sleep as needed

//   // Assuming OTP is '5555', prepare payload for verification
//   const payload = JSON.stringify({
//     "phone": phone,
//     "otp": "5555",
//     "deviceInfo": {
//       "APP_TYPE": "android",
//       "DeviceData": {
//         "deviceUID": "36e27f877d1a7c24"
//       }
//     },
//     "utmPayload": {},
//     "campaignUrl": "",
//     "sessionId": null,
//     "referralCode": null,
//     "provider": ""
//   });

//   // Verify OTP
//   const verifyOtpResponse = http.post(`${BASE_URL}/api/v4/verify/otp`, payload, { headers });
//   check(verifyOtpResponse, {
//     "OTP verified successfully for different numbers": (r) => r.status === 200 || r.status === 400
//   });

//   // Log based on verification result
//   if (verifyOtpResponse.status === 200 || verifyOtpResponse.status === 400) {
//     console.log(`OTP verified successfully for ${phone}.`);
//   } else {
//     console.log(`Verification failed for ${phone}.`);
//   }

//   console.log(`Response body for ${phone}: ${verifyOtpResponse.body}`);
//   sleep(1); // Adjust sleep as needed
  
// }

