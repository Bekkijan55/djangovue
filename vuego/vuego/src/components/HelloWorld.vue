<template>
  <div class="container"></div>
</template>

<script>
import axios from "axios";
import { mapGetters } from "vuex";
export default {
  name: "HelloWorld",
  data() {
    return {
      msg: ''
    };
  },

  mounted() {
    this.getTasks();
  },

  computed: {
    ...mapGetters(["allTasks"])
  },

  methods: {
    getTasks() {
      this.$store.dispatch("getAllTasks");

      console.log(this.allTasks);
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.select,
select {
  /* 100% width for the select */
  width: 100%;
}

.card {
  /* Adding some air under the tasks */
  margin-bottom: 25px;
}

.done {
  /* Make the done tasks a little bit transparent */
  opacity: 0.3;
}
</style>
