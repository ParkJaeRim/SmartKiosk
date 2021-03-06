import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueCookies from 'vue-cookies';
import store from './store'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import { FormGroupPlugin } from 'bootstrap-vue'
Vue.use(FormGroupPlugin)
/* eslint-disable no-new */
import { NavbarPlugin } from 'bootstrap-vue'
Vue.use(NavbarPlugin)
// Install BootstrapVue
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)
Vue.use(VueCookies);

new Vue({
  el: '#app',
  router,
  store, 
  components: { App }, 
  template: '<App/>'
})
 