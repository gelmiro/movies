import Vue from 'vue'
import Router from 'vue-router'
import Movie from "../views/Movie";
import Login from "../views/Login";
import Register from "../views/Register";
import Favourite from "../views/Favourite"

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      redirect: '/movies',

    },
    {
      name: 'movies',
      path: '/movies',
      component: Movie,
    },
    {
      name: 'login',
      path: '/login',
      component: Login,
    },
    {
      name: 'register',
      path: '/register',
      component: Register,
    },
    {
      name: 'favourites',
      path: '/favourites',
      component: Favourite,
    }
  ]
})


export default router
