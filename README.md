# My Choice API

Heroku App: https://mychoicebe.herokuapp.com/

API Documentation: https://mychoicebe.herokuapp.com/swagger-ui/

## VOTE
Endpoint: `/vote/<election-id>`

### GET

**FORMAT**
```
{
  'election': <ELECTION OBJECT>, 
  'position_candidates': 
  {
    ...
    <POSITION OBJECT>: <QuerySet [<CANDIDATE OBJECT>, <CANDIDATE OBJECT>]>, 
    ...
  }  
}
```

**EXAMPLE**
```
{
  'election': <Election: 2020 General Election>, 
  'position_candidates': 
  {
    <Position: President | 2020 General Election>: <QuerySet [<Candidate: Donald Trump>, <Candidate: Joe Biden>]>, 
    <Position: Vice President | 2020 General Election>: <QuerySet [<Candidate: Kamala Harris>, <Candidate: Mike Pence>]>, 
    <Position: Region 1 Senator | 2020 General Election>: <QuerySet []>
  }  
}
```

Candidate Object Properties:
* id 
* first_name
* last_name
* picture_self
* party
* gender
* ethnicity
* votes

Position Object Properties:
* id
* name
* locality

Election Object Properties:
* id
* title
* start_time
* end_time

### POST 

**FORMAT**
```
<QueryDict: {
  'csrfmiddlewaretoken': ['this-is-some-token'], 
  '<POSITION NAME>': ['<CANDIDATE ID>']
  ...
}>
```
**EXAMPLE**
```
<QueryDict: {
  'csrfmiddlewaretoken': ['Pg5whBoPqXByENCMxrs8iMZ0RqnNgf5HOWnOoZBuCHf7xGN88eyDax6ABiLCIPVp'], 
  'President': ['1'], 
  'Vice President': ['3']
}>
```

## RESULTS

**GET (equivalent to GET request of VOTE)**

**FORMAT**
```
{
  'election': <ELECTION OBJECT>, 
  'position_candidates': 
  {
    ...
    <POSITION OBJECT>: <QuerySet [<CANDIDATE OBJECT>, <CANDIDATE OBJECT>]>, 
    ...
  }  
}
```

**EXAMPLE**
```
{
  'election': <Election: 2020 General Election>, 
  'position_candidates': 
  {
    <Position: President | 2020 General Election>: <QuerySet [<Candidate: Donald Trump>, <Candidate: Joe Biden>]>, 
    <Position: Vice President | 2020 General Election>: <QuerySet [<Candidate: Kamala Harris>, <Candidate: Mike Pence>]>, 
    <Position: Region 1 Senator | 2020 General Election>: <QuerySet []>
  }  
}
```
