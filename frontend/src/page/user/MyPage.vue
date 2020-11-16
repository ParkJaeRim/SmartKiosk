<template>
  <b-container>
<order-list />      
  </b-container>
</template>

<script>
import OrderList from '../../components/User/OrderList.vue'
import UserInfo from '../../components/User/UserInfo.vue'

export default {
  name: "MyPage",
  components:{
    OrderList,
    UserInfo,
  },
};
</script>

<style scoped>
.container {
  background-color: white;
  padding: 0;
}
h1{
  margin-bottom:50px;
}
</style>
