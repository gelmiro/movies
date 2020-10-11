import Vue from 'vue'
import VueAxios from 'vue-axios'
import axios from "axios";
import router from '../router'
import jwt_decode from 'jwt-decode'

Vue.use(VueAxios, axios)
Vue.axios.defaults.baseURL = 'http://dev4.scout.wro.nsn-rdnet.net/api/v1/'

Vue.axios.interceptors.request.use(function(config) {
  const authorization = config.headers.Authorization
  if (authorization) {
    const token = authorization.replace('JWT ', '')
    try {
      const {exp} = jwt_decode(token)
      if (!exp || (new Date(0).setUTCSeconds(exp) <= new Date().valueOf())) {
        router.push({name: 'login'})
        return
      }
    } catch {
      router.push({name: 'login'})
    }

  }
  return config;
}, function(error) {
  return Promise.reject(error);
});