import json

from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
import requests as r
from starterkit.settings import API_2GIS_KEY
from .models import Place
# Create your views here.
from api.v1.apps.users.models import User
from api.v1.apps.users.serializers import UserSerializer

PARAMS = '&fields=items.point,items.full_address_name,items.schedule,items.photos,items.contact_groups,items.rubrics,items.statistics,items.description,items.links&locale=ru_RU&type=branch'


def get_user(request):
    user_id = UserSerializer(request.user).data['id']
    user = User.objects.get(id=user_id)
    return user


class PlacesView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        search_query = request.data['search_query']
        req_json = None
        if 'cords' in request.data or 'city_id' in request.data:
            if 'cords' in request.data:
                cords = request.data['cords']
                query_string = f'?sort_point={cords[0]},{cords[1]}&'
                for key in list(search_query.keys()):
                    query_string += f'{key}={search_query[key]}&'
                req = r.get(f'https://catalog.api.2gis.com/3.0/items{query_string}&key={API_2GIS_KEY}{PARAMS}')
                req_json = json.loads(req.text)

            if 'city_id' in request.data:
                city_id = request.data['city_id']
                query_string = f'?city_id={city_id}&'
                for key in list(search_query.keys()):
                    query_string += f'{key}={search_query[key]}&'
                req = r.get(f'https://catalog.api.2gis.com/3.0/items{query_string}&key={API_2GIS_KEY}')
                req_json = json.loads(req.text)

            if 'error' in req_json:
                return Response({'status': False, 'msg': req_json['error']})
            else:
                return Response({'status': True, 'items': req_json['result']['items']})

        return Response({'status': False, 'msg': "City_id or cords are must be in request"})


class AddToVisited(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        id_2gis = request.data['2gis_id']
        user = get_user(request)
        place = Place.objects.create(id_2gis=id_2gis)
        user.frequently_visited_places.add(place)
        # user.favorite_placess.add(place)
        user.save()
        return Response({'status': True, 'msg': 'Successful!'})


class AddToFavourite(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        id_2gis = request.data['2gis_id']
        user = get_user(request)
        place = Place.objects.create(id_2gis=id_2gis)
        user.frequently_visited_places.add(place)
        user.favorite_places.add(place)
        user.save()
        return Response({'status': True, 'msg': 'Successful!'})


class GetFavList(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = get_user(request)
        req_json = None
        fav_list = user.favorite_places.all()
        if 'search_query' in request.data:
            search_query = request.data['search_query']
            query_string = ''
            for key in list(search_query.keys()):
                query_string += f'{key}={search_query[key]}&'
            query_string += 'id='
            for fav in fav_list:
                query_string += fav.id_2gis + ','
            req = r.get(f'https://catalog.api.2gis.com/3.0/items/byid?{query_string}&key={API_2GIS_KEY}{PARAMS}')
            req_json = json.loads(req.text)
        else:
            query_string = 'id='
            for fav in fav_list:
                query_string += fav.id_2gis + ','
            req = r.get(f'https://catalog.api.2gis.com/3.0/items/byid?{query_string}&key={API_2GIS_KEY}{PARAMS}')
            req_json = json.loads(req.text)
        if 'error' in req_json:
            return Response({'status': False, 'msg': req_json['error']})
        else:
            return Response({'status': True, 'items': req_json['result']['items']})

class GetWatchList(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = get_user(request)
        req_json = None
        watch_list = user.frequently_visited_places.all()
        if 'search_query' in request.data:
            search_query = request.data['search_query']
            query_string = ''
            for key in list(search_query.keys()):
                query_string += f'{key}={search_query[key]}&'
            query_string += 'id='
            for fav in watch_list:
                query_string += fav.id_2gis + ','
            req = r.get(f'https://catalog.api.2gis.com/3.0/items/byid?{query_string}&key={API_2GIS_KEY}{PARAMS}')
            req_json = json.loads(req.text)
        else:
            query_string = 'id='
            for fav in watch_list:
                query_string += fav.id_2gis + ','
            req = r.get(f'https://catalog.api.2gis.com/3.0/items/byid?{query_string}&key={API_2GIS_KEY}{PARAMS}')
            req_json = json.loads(req.text)
        if 'error' in req_json:
            return Response({'status': False, 'msg': req_json['error']})
        else:
            return Response({'status': True, 'items': req_json['result']['items']})



class GetOnePlace(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        id_2gis = request.data['2gis_id']
        req = r.get(f'https://catalog.api.2gis.com/3.0/items/byid?id={id_2gis}&key={API_2GIS_KEY}{PARAMS}')
        req_json = json.loads(req.text)
        if 'error' in req_json:
            return Response({'status': False, 'msg': req_json['error']})
        else:
            return Response({'status': True, 'items': req_json['result']['items']})