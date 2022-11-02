<template>
  <div class="border">
      <h1>{{ msgTitle }}</h1>
      <MyComponentItem msg-title="하위 컴포넌트"
      :dynamic-props="dynamicProps"
      @child-to-parent="parentGetEvent"
      @child-input="getDynamicData"
      />
  </div>
</template>

<script>
import MyComponentItem from '@/components/MyComponentItem'

export default {
    name: 'MyComponent',
    components: {
        MyComponentItem,
    },
    data: function() {
      return {
        dynamicProps:'이건 동적인 데이터',
      }
    },
    methods: {
      parentGetEvent: function(childData) {
        console.log('자식 컴포넌트에서 발생한 emit 이벤트를 들었다!')
        console.log(childData)
      },
      getDynamicData: function(childInputData) {
        console.log(`사용자가 입력한 값은 ${childInputData}입니다.`)
      },
    },
    props: {
    msgTitle: String
    }
}
</script>

<style>

</style>