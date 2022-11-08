<template>
  <div>
    <button @click="picksize" style="width:100%; padding:11.7%;" :class="{'is-selected' : size.selected}">
      <span style="float:left">{{size.name}}</span> 
      <span style="float:right">{{size.price}}원</span>
    </button>
  </div>
</template>

<script>
export default {
  name: 'SizeListItem',
  props: {
    size: Object,
  },
  methods: {
    picksize() {
      this.$store.dispatch('picksize',this.size)
    }
  }
}
</script>

<style>

.is-selected {
  background-color : greenyellow;
}

</style>