# API Bafomet Backend

## Base url `http://bafomet.wellbe.club`

## Аунтефикация

### Регистрация
#### Send Confirm email
Request

    Method POST
    api/v1/users/auth/registrate/send_email/
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
    api/v1/users/auth/registrate/confirm_email/
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
    api/v1/users/auth/registrate/me/
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
    api/v1/users/auth/token/
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
    api/v1/users/auth/token/refresh/
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
    api/v1/places/place/
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
      'items': [{
            "address_name": "Ленина проспект, 46/2",
            "contact_groups": [
                {
                    "contacts": [
                        {
                            "type": "phone",
                            "text": "+7‒963‒018‒10‒04",
                            "print_text": "+7‒963‒018‒10‒04",
                            "value": "+79630181004"
                        }
                    ]
                }
            ],
            "full_address_name": "Губаха, Ленина проспект, 46/2",
            "id": "70000001042208522_4r6fg8G6G73H0H7J272H9772yjo5755942332172huvjvH19065GI4J5I2H0Aerkd9815802003318643JJH0JIJGJI029",
            "name": "Шаверма №1",
            "point": {
                "lat": 58.836511,
                "lon": 57.555528
            },
            "rubrics": [
                {
                    "alias": "kafe",
                    "id": "161",
                    "kind": "primary",
                    "name": "Кафе",
                    "parent_id": "2",
                    "short_id": 161
                },
                {
                    "alias": "uchastniki_proekta_sberryadom",
                    "id": "112537",
                    "kind": "additional",
                    "name": "Участники проекта СберРядом",
                    "parent_id": "969",
                    "short_id": 112537
                }
            ],
            "schedule": {
                "Fri": {{
            "address_name": "Ленина проспект, 46/2",
            "contact_groups": [
                {
                    "contacts": [
                        {
                            "type": "phone",
                            "text": "+7‒963‒018‒10‒04",
                            "print_text": "+7‒963‒018‒10‒04",
                            "value": "+79630181004"
                        }
                    ]
                }
            ],
            "full_address_name": "Губаха, Ленина проспект, 46/2",
            "id": "70000001042208522_4r6fg8G6G73H0H7J272H9772yjo5755942332172huvjvH19065GI4J5I2H0Aerkd9815802003318643JJH0JIJGJI029",
            "name": "Шаверма №1",
            "point": {
                "lat": 58.836511,
                "lon": 57.555528
            },
            "rubrics": [
                {
                    "alias": "kafe",
                    "id": "161",
                    "kind": "primary",
                    "name": "Кафе",
                    "parent_id": "2",
                    "short_id": 161
                },
                {
                    "alias": "uchastniki_proekta_sberryadom",
                    "id": "112537",
                    "kind": "additional",
                    "name": "Участники проекта СберРядом",
                    "parent_id": "969",
                    "short_id": 112537
                }
            ],
            "schedule": {
                "Fri": {
                    "working_hours": [
                        {
                            "from": "10:00",
                            "to": "22:30"
                        }
                    ]
                },
                "Mon": {
                    "working_hours": [
                        {
                            "from": "10:00",
                            "to": "22:30"
                        }
                    ]
                },
                "Sat": {
                    "working_hours": [
                        {
                            "from": "10:00",
                            "to": "22:30"
                        }
                    ]
                },
                "Sun": {
                    "working_hours": [
                        {
                            "from": "10:00",
                            "to": "22:30"
                        }
                    ]
                },
                "Thu": {
                    "working_hours": [
                        {
                            "from": "10:00",
                            "to": "22:30"
                        }
                    ]
                },
                "Tue": {
                    "working_hours": [
                        {
                            "from": "10:00",
                            "to": "22:30"
                        }
                    ]
                },
                "Wed": {
                    "working_hours": [
                        {
                            "from": "10:00",
                            "to": "22:30"
                        }
                    ]
                }
            },
            "type": "branch"
        },
        {
            "address_name": "Пугачёва, 25",
            "contact_groups": [
                {
                    "contacts": [
                        {
                            "type": "phone",
                            "text": "+7 (34271) 2‒58‒76",
                            "print_text": "+7 (34271) 2‒58‒76",
                            "value": "+73427125876"
                        },
                        {
                            "type": "instagram",
                            "text": "https://instagram.com/japonka_kungur",
                            "value": "https://instagram.com/japonka_kungur",
                            "url": "https://instagram.com/japonka_kungur"
                        },
                        {
                            "type": "vkontakte",
                            "text": "https://vk.com/yaponka_kyngyr",
                            "value": "https://vk.com/yaponka_kyngyr",
                            "url": "https://vk.com/yaponka_kyngyr"
                        }
                    ]
                }
                    "working_hours": [
                        {
                            "from": "10:00",
                            "to": "22:30"
                        }
                    ]
                },
                "Mon": {
                    "working_hours": [
                        {
                            "from": "10:00",
                            "to": "22:30"
                        }
                    ]
                },
                "Sat": {
                    "working_hours": [
                        {
                            "from": "10:00",
                            "to": "22:30"
                        }
                    ]
                },
                "Sun": {
                    "working_hours": [
                        {
                            "from": "10:00",
                            "to": "22:30"
                        }
                    ]
                },
                "Thu": {
                    "working_hours": [
                        {
                            "from": "10:00",
                            "to": "22:30"
                        }
                    ]
                },
                "Tue": {
                    "working_hours": [
                        {
                            "from": "10:00",
                            "to": "22:30"
                        }
                    ]
                },
                "Wed": {
                    "working_hours": [
                        {
                            "from": "10:00",
                            "to": "22:30"
                        }
                    ]
                }
            },
            "type": "branch"
        },
        {
            "address_name": "Пугачёва, 25",
            "contact_groups": [
                {
                    "contacts": [
                        {
                            "type": "phone",
                            "text": "+7 (34271) 2‒58‒76",
                            "print_text": "+7 (34271) 2‒58‒76",
                            "value": "+73427125876"
                        },
                        {
                            "type": "instagram",
                            "text": "https://instagram.com/japonka_kungur",
                            "value": "https://instagram.com/japonka_kungur",
                            "url": "https://instagram.com/japonka_kungur"
                        },
                        {
                            "type": "vkontakte",
                            "text": "https://vk.com/yaponka_kyngyr",
                            "value": "https://vk.com/yaponka_kyngyr",
                            "url": "https://vk.com/yaponka_kyngyr"
                        }
                    ]
                }]
    }


## Работа с личным кабинетом
### /me
Request
    
    Method GET
    api/v1/users/auth/me
    Token in header
Response

    {
      ''
    }
### Получить избранные магазины пользователя
Request

    Method POST
    api/v1/users/auth
Response

    Access-token

### Добавить магазин в избранное
Request

    Method POST
    api/v1/users/auth
Response

    Access-token    