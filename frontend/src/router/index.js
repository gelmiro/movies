import Vue from 'vue'
import Router from 'vue-router'
import Movie from "../views/Movie";
import Login from "../views/Login";
import Register from "../views/Register";
import Favourite from "../views/Favourite"
import Authentication from "../views/Authentication";
import Home from "../views/Home";

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      redirect: '/movies',

    },
    {
      name: 'authentication',
      path: '',
      component: Authentication,
      children: [
        {
          name: 'login',
          path: '/login',
          component: Login,
        },
        {
          name: 'register',
          path: '/register',
          component: Register,
        }
      ]
    },
    {
      name: 'home',
      path: '',
      component: Home,
      children: [
        {
          name: 'movies',
          path: '/movies',
          component: Movie,
        },
        {
          name: 'favourites',
          path: '/favourites',
          component: Favourite,
        }
      ]
    },
    {
      path: '/*',
      redirect: '/movies',
    }
  ]
})


export default router
