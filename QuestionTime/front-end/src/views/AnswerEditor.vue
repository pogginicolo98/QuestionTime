<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col-12">
        <h1 class="mb-3">Edit your answer</h1>
        <form @submit.prevent="onSubmit">
          <textarea
            v-model="answerBody"
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
    previousAnswer: {
      type: String,
      required: true
    },
    questionSlug: {
      type: String,
      required: true
    }
  },
  async beforeRouteEnter(to, from, next) {
    let endpoint = `/api/answers/${to.params.id}/`;
    await apiService(endpoint)
            .then(answerData => {
              to.params.previousAnswer = answerData.body;
              to.params.questionSlug = answerData.question_slug;
            });
    return next();
  },
  data() {
    return {
      answerBody: this.previousAnswer,
      error: null
    }
  },
  methods: {
    onSubmit() {
      if (this.answerBody) {
        let endpoint = `/api/answers/${this.id}/`;
        let method = "PUT";
        let data = { body: this.answerBody };
        apiService(endpoint, method, data)
          .then(() => {
            this.$router.push({
              name: "question",
              params: { slug: this.questionSlug }
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
