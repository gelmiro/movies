import Vue from 'vue'
import Router from 'vue-router'
import Movie from "../views/Movie";
import Login from "../views/Login";
import Register from "../views/Register";
import Favourite from "../views/Favourite"
import store from '../store'

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
      meta: {
        publicContent: true
      },
    },
    {
      name: 'register',
      path: '/register',
      component: Register,
      meta: {
        publicContent: true
      },
    },
    {
      name: 'favourites',
      path: '/favourites',
      component: Favourite,
    }
  ]
})

router.beforeEach((to, from, next) => {
  const publicContent = to.matched.some(record => record.meta.publicContent)
  if (!publicContent) {
    const expiration = store.state.authentication.user.exp
    console.log('time left to expiration', (new Date(0).setUTCSeconds(expiration) -  new Date().valueOf()) / 1000)
    if (!expiration || (new Date(0).setUTCSeconds(expiration) <= new Date().valueOf())) {
      next({name: 'login'})
      return
    }
  }
  next()
})
console.log('router', router)
export default router
