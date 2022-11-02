<template>
  <div>
    <h4>{{ msgTitle }}</h4>
    <p>{{ dynamicProps }}</p>
    <input 
    type="text"
    v-model="childInputData"
    @keyup.enter="childInput">
    <button @click="childToParent">클릭!</button>
  </div>
</template>

<script>

export default {
    name: "MyComponentItem",
    props: {
      msgTitle: String,
      dynamicProps: String,
    },
    data: function() {
      return {
        childInputData: null,
      }
    },
    methods: {
      childToParent: function() {
        this.$emit('child-to-parent', '나는 자식이 보낸 데이터다')
      },
      childInput: function() {
        this.$emit('child-input',this.childInputData)
        this.childInputData = null
      }
    },
}
</script>

<style>

</style>