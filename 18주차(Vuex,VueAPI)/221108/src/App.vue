<template>
  <div id="app">
    <h1 style="text-align:center;">Coffee Order App</h1>
    <div style="display:flex">
      <div style="width:33%;">
        <MenuList/>
      </div>
      <div style="width:33%;">
        <SizeList/>
      </div>
      <div style="width:33%;">
        <OptionList/>
      </div>
    </div>
    <div>
      <button @click="pickorder" style="width:100%;">장바구니 담기</button>
    </div>
    <OrderList/>
  </div>
</template>

<script>
import MenuList from '@/components/MenuList/'
import SizeList from '@/components/SizeList/'
import OrderList from '@/components/OrderList/'
import OptionList from '@/components/OptionList/'

export default {
  name: 'App',
  components: {
    MenuList,
    SizeList,
    OrderList,
    OptionList,
  },
  methods: {
    pickorder() {
      this.$store.dispatch("pickorder")
    }
  },
  computed: {
  }
}
</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
  padding: 0;
  margin: 0;
}

ul {
  list-style: none;
}
</style>
