# API Bafomet Backend

## Base url `http://bafomet.wellbe.club`

## Аунтефикация

### Регистрация
#### Send Confirm email
Request

    Method POST
    api/v1/users/registrate/send_email/
    {
      'email': string
    }
Response

    {
      'status': bool,
      'mes': string
    }  
####  Confirm Email OTP
Request

    Method POST
    api/v1/users/registrate/confirm_email/
    {
      'email': string,
      'otp': string
    }
Response

    {
      'status': bool,
      'mes': string
    }  
####  Confirm Email OTP
Request

    Method POST
    api/v1/users/registrate/me/
    {
      'email': string,
      'name': string,
      'password': string
    }
Response

    {
      'status': bool,
      'detail': string
    }  

### Авторизация
#### Get Access and Refresh Tokens (Login)
Request

    Method POST
    /v1/users/auth/token/
    {
      'email': string,
      'password': string
    }
Response

    {
      'access': string,
      'refresh': string
    }  
#### Get Access Token by refresh (Relogin)
Request

    Method POST
    /v1/users/auth/token/refresh/
    {
      'refresh': string,
    }
Response

    {
      'access': string,
    }  


## Поиск с 2GIS API

### Поиск магазинов вокруг геолокации
Request

    Method POST
    /v1/places/place/
    {
      # City_id or cords required
      'city_id': 'string', - not required
      'cords': [float, float], - not required
      'search_query':
      {
        -params as 2gis_api ('q' : ' КОфе')
      }  
    }
Response

    {
      'status': bool, 
      'items': [{with }]
    }

### Поиск магазинов в городе
Request

    Method POST
    /v1/users/auth
Response

    Access-token

## Работа с личным кабинетом

### Получить избранные магазины пользователя
Request

    Method POST
    /v1/users/auth
Response

    Access-token

### Добавить магазин в избранное
Request

    Method POST
    /v1/users/auth
Response

    Access-token    