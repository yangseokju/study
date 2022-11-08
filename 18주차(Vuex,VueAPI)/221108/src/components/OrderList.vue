<template>
  <div>
    <h2><b>주문 내역</b></h2>
    <h3>총 {{totalOrderCount}}건: {{totalOrderPrice}}</h3>
    <div>
      <ul>
        <OrderListItem
        v-for="(order, index) in orderList"
        :key="index"
        :order="order"
        />
      </ul>
    </div>
  </div>
</template>

<script>
import OrderListItem from '@/components/OrderListItem/'

export default {
  name: 'OrderList',
  components: {
    OrderListItem,
  },
  computed: {
    orderList() {
      return this.$store.state.orderList
    },
    totalOrderCount: function () {
      return this.$store.getters.totalOrderCount
    },
    totalOrderPrice: function () {
      return this.$store.getters.totalOrderPrice
    },
  },
}
</script>

<style>
</style>