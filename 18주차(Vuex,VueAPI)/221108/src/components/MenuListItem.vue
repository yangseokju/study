<template>
  <div>
    <button @click="pickmenu" style="width:100%; padding:6.8%;" :class="{'is-selected' : menu.selected}">
      <img :src="menu.image" style="float:left" width="50px" height="50px"> 
      <span style="float:center">{{menu.title}}</span> 
      <span style="float:right">{{menu.price}}원</span>
    </button>
  </div>
</template>

<script>

export default {
  name: 'MenuListItem',
  props: {
    menu: Object,
  },
  methods: {
    pickmenu() {
      this.$store.dispatch('pickmenu', this.menu)
    }
  },
}

</script>

<style>

.is-selected {
  background-color : greenyellow;
}

</style>