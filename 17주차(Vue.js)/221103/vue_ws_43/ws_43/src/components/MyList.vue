<template>
    <div class="box divright" style="height:inherit; padding:50px;">
        <h2>상담 신청 현황</h2>
        <h3>상담 선생님</h3>
        <h4>성함 :
          <span v-for="(teacher, i) in timeSelected" :key="i">
            {{teacher}}
          </span>
        </h4>
        <hr>
        <h3>예약 현황</h3>
        <h4>시간들 : 
          <span v-for="(select, j) in teacherSelected" :key="j">
            {{select}}
          </span>
        </h4>
        <hr>
        <img alt="ssafy_logo" src="@/assets/ssafy-logo.png">
      </div>
</template>

<script>
export default {
    name:'MyList',
    props: {
        teacherSelected: Array,
        timeSelected: Array,
    },
}
</script>

<style>

</style>