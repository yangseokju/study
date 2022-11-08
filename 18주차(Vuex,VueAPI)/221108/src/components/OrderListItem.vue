<template>
  <li>
    <div style="display: flex; margin:20px;">
      <img :src="order.menu.image" style="width:100px; height:100px;">
      <div>
        <p>{{order.menu.title}}</p> 
        <p>사이즈: {{order.size.name}}</p>
      </div>
      <span style="width:100%">
        <span style="float:right">가격 : {{getPrice}}원</span>
      </span>
    </div>
    <hr>
  </li>
</template>

<script>
export default {
  name: 'OrderListItem',
  props: {
    order: Object,
  },
  computed: {
    getPrice() {
      let getPrice = this.order.menu.price + this.order.size.price
      return getPrice
    },
  },
}
</script>

<style>
</style>