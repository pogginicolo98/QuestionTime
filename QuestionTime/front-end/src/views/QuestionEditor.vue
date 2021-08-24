<template lang="html">
  <div v-if="notFound" class="container">
    <h1 class="notFound">Question not found!</h1>
  </div>
  
  <div v-else class="container">
    <div class="row">
      <div class="col-12">
        <h1 class="mb-3">Ask a new question</h1>
        <form @submit.prevent="onSubmit">
          <textarea
            v-model="questionBody"
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
  props: {
    slug: {
      type: String,
      required: false
    },
    previousQuestion: {
      type: String,
      required: false
    },
    questionNotFound: {
      type: String,
      required: false
    }
  },
  data() {
    return {
      questionBody: this.previousQuestion || null,
      error: null
    }
  },
  async beforeRouteEnter(to, from, next) {
    if(to.params.slug !== undefined) {
      let endpoint = `/api/questions/${to.params.slug}/`;
      await apiService(endpoint)
              .then(questionData => {
                to.params.previousQuestion = questionData.content;
                to.params.questionNotFound = questionData.detail;
              });
    }
    return next();
  },
  computed: {
    notFound() {
      return this.questionNotFound;
    }
  },
  methods: {
    onSubmit() {
      if (!this.questionBody) {
        this.error = "The question cannot be empty.";
      } else if (this.questionBody.length > 240) {
        this.error = `The question is too long. ${this.questionBody.length}/240 characters.`;
      } else {
        let endpoint = "/api/questions/";
        let method = "POST";
        if(this.previousQuestion) {
          endpoint += `${this.slug}/`;
          method = "PUT";
        }
        let data = { content: this.questionBody };
        apiService(endpoint, method, data)
          .then(questionData => {
            this.$router.push({
              name: "question",
              params: { slug: questionData.slug }
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
