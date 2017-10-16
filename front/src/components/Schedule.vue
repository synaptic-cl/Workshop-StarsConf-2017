<template>
  <div class="schedule">
    <pre>{{$data}}</pre>
  </div>
</template>

<script>
import TASKS_ALL from '../graphql/AllTalks.gql'

export default {
  name: 'schedule',
  components: {
  },

  data() {
    return {
      tasks: [],
      addMode: false,
    }
  },

  apollo: {
    tasks: {
      query: TASKS_ALL,
      update({ allTalks }) {
        return allTalks
      },
    },
  }
}
</script>


<style>

</style>