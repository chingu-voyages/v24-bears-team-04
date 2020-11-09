# My Choice API

Heroku App: https://mychoicebe.herokuapp.com/

API Documentation: https://mychoicebe.herokuapp.com/swagger-ui/

## VOTE AND RESULTS
Endpoint: `/vote/<election-id>`

### GET

**FORMAT**
```
{
  "id": <ELECTION ID>,
  "position_set": [
    {
      "id": <POSITION-ID>,
      "candidate_set": [
        ...
        {
          "id": <CANDIDATE ID>,
          "first_name": "",
          "last_name": "",
          "picture_self": null,
          "party": "",
          "gender": "",
          "ethnicity": "",
          "votes": 0,
          "positions": [
            ...
            <POSITION ID>,
            ...        
          ]
        }
        ...
      ],
      "name": "<POSITION NAME>",
      "locality": "<LOCALITY NAME>",
      "seats": 1,
      "election": <ELECTION ID>
    }
  ],
  "title": "<ELECTION TITLE>",
  "start_time": "2020-11-01T00:00:00Z",
  "end_time": "2020-11-04T00:00:00Z"
}
```

**EXAMPLE**
```
{
  "id": 3,
  "position_set": [
    {
      "id": 1,
      "candidate_set": [
        {
          "id": 2,
          "first_name": "Donald",
          "last_name": "Trump",
          "picture_self": null,
          "party": "Other",
          "gender": "Male",
          "ethnicity": "",
          "votes": 2,
          "positions": [
            1,
            4
          ]
        },
        {
          "id": 1,
          "first_name": "Joe",
          "last_name": "Biden",
          "picture_self": null,
          "party": "Other",
          "gender": "Male",
          "ethnicity": "",
          "votes": 5,
          "positions": [
            1,
            5
          ]
        }
      ],
      "name": "President",
      "locality": "USA",
      "seats": 1,
      "election": 3
    },
    {
      "id": 2,
      "candidate_set": [
        {
          "id": 3,
          "first_name": "Kamala",
          "last_name": "Harris",
          "picture_self": null,
          "party": "Other",
          "gender": "Female",
          "ethnicity": "",
          "votes": 4,
          "positions": [
            2
          ]
        },
        {
          "id": 4,
          "first_name": "Mike",
          "last_name": "Pence",
          "picture_self": null,
          "party": "Other",
          "gender": "Male",
          "ethnicity": "",
          "votes": 1,
          "positions": [
            2
          ]
        }
      ],
      "name": "Vice President",
      "locality": "USA",
      "seats": 1,
      "election": 3
    },
    {
      "id": 3,
      "candidate_set": [],
      "name": "Region 1 Senator",
      "locality": "R1",
      "seats": 2,
      "election": 3
    }
  ],
  "title": "2020 General Election",
  "start_time": "2020-11-01T00:00:00Z",
  "end_time": "2020-11-04T00:00:00Z"
}
```

### POST 

**FORMAT**
```
{
  ...
  "<POSITION ID>": "<CANDIDATE ID>",
  ...
}
```
**EXAMPLE**
```
{
  ...
  "1": "2",
  ...
}
```
