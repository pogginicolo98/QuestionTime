<template lang="html">
  <div class="container">
    <div class="row">
      <div class="col-12">
        <h1 class="mb-3">Ask a new question</h1>
        <form @submit.prevent="onSubmit">
          <textarea
            v-model="question_body"
            class="form-control"
            rows="3"
            placeholder="Your question...">
          </textarea>
          <br>
          <button class="btn btn-success" type="submit">Post question</button>
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
  name: "QuestionEditor",
  data() {
    return {
      question_body: null,
      error: null
    }
  },
  methods: {
    onSubmit() {
      if (!this.question_body) {
        this.error = "The question cannot be empty.";
      } else if (this.question_body.length > 240) {
        this.error = `The question is too long. ${this.question_body.length}/240 characters.`;
      } else {
        let endpoint = "/api/questions/";
        let method = "POST";
        let data = { content: this.question_body };
        apiService(endpoint, method, data)
          .then(question_data => {
            this.$router.push({
              name: "question",
              params: { slug: question_data.slug }
            });
          });
      }
    }
  },
  created() {
    document.title = "New Question";
  }
}
</script>

<style lang="css" scoped>
</style>
