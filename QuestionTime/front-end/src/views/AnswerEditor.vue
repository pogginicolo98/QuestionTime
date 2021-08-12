<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col-12">
        <h1 class="mb-3">Edit your answer</h1>
        <form @submit.prevent="onSubmit">
          <textarea
            v-model="answer_body"
            class="form-control"
            rows="3">
          </textarea>
          <br>
          <button class="btn btn-success" type="submit">Edit answer</button>
        </form>
        <p class="text-danger mt-2">{{ error }}</p>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { apiService } from "@/common/api.service.js";

export default {
  name: "AnswerEditor",
  props: {
    id: {
      type: Number,
      required: true
    },
    answer_edit: {
      type: String,
      required: true
    },
    question_slug: {
      type: String,
      required: true
    }
  },
  async beforeRouteEnter(to, from, next) {
    let endpoint = `/api/answers/${to.params.id}/`;
    await apiService(endpoint)
            .then(answer_data => {
              to.params.answer_edit = answer_data.body;
              to.params.question_slug = answer_data.question_slug;
            });
    return next();
  },
  data() {
    return {
      answer_body: this.answer_edit,
      error: null
    }
  },
  methods: {
    onSubmit() {
      if (this.answer_body) {
        let endpoint = `/api/answers/${this.id}/`;
        let method = "PUT";
        let data = { body: this.answer_body };
        apiService(endpoint, method, data)
          .then(() => {
            this.$router.push({
              name: "question",
              params: { slug: this.question_slug }
            });
          })
      } else {
        this.error = "The question cannot be empty."
      }
    }
  }
}
</script>

<style lang="css" scoped>
</style>
