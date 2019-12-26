// import '@babel/polyfill'
import Vue from 'vue'
import App from './App.vue'
import router from './router/index'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import './assets/bootstrap/css/bootstrap.min.css';
import iView from 'view-design';
import 'view-design/dist/styles/iview.css';
import * as $http from './requests/index';
import * as $service from './services/index'
import echarts from 'echarts';

Vue.prototype.api = "http://192.168.1.179:8000"
Vue.prototype.$http = $http
Vue.prototype.$echarts = echarts
Vue.prototype.$service = $service
Vue.config.productionTip = false
Vue.use(ElementUI);
Vue.use(iView);

// 全局导航守卫
router.beforeEach((to, from, next) => {
  // document.title = to.name; // 让页面title显示路由对应的name值
  let user = JSON.parse(sessionStorage.getItem("manageuser"));
  if (to.path === '/system_Login') {
    sessionStorage.removeItem("manageuser");
  }
  if (to.meta.requireAuth) { // 判断该路由是否需要登录权限
    if (user) { //判断本地是否存在user
      next();
    } else {
      if (to.path === '/account/register') {
        next();
      } else {
        next({
          path: '/system_Login'
        })
      }
    }
  }
  else {
    next();
  }
})


new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
