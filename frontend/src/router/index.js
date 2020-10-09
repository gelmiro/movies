import Vue from 'vue'
import Router from 'vue-router'
import Movie from "../views/Movie";

Vue.use(Router)

const router = new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      redirect: '/movies'
    },
    {
      path: '/movies',
      component: Movie,
    }
  ]
})

export default router
