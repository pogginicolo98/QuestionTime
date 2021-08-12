<template>
  <div class="home-view">
    <div class="container">
      <div class="mt-2">
        <div v-for="question in questions"
             :key="question.id">
          <p class="mb-0">
            Question written by:
            <span class="author-name">{{ question.author }}</span>
          </p>
          <h2>
            <router-link
              :to="{ name: 'question', params: { slug: question.slug } }"
              class="question-link">
              {{ question.content }}
            </router-link>
          </h2>
          <p>Answers: {{ question.answers_count }}</p>
          <hr>
        </div>
      </div>
      <div class="my-4 text-center" >
        <div v-show="loadingQuestions">
          <div class="spinner-border text-danger mt-3"
               style="width: 3rem; height: 3rem;"
               role="status">
          </div>
        </div>
        <button
          v-show="next"
          @click="getQuestions"
          class="btn btn-danger mt-4">
          Show more
        </button>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { apiService } from "@/common/api.service.js";

export default {
  name: "Home",
  data() {
    return {
      questions: [],
      next: null,
      loadingQuestions: false
    };
  },
  methods: {
    getQuestions() {
      let endpoint = "/api/questions/";
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingQuestions = true;
      apiService(endpoint)
        .then(questionsData => {
          this.questions.push(...questionsData.results);
          this.loadingQuestions = false;
          if (questionsData.next) {
            this.next = questionsData.next;
          } else {
            this.next = null;
          }
        });
    }
  },
  created() {
    this.getQuestions();
    document.title = "QestionTime";
  }
};
</script>

<style lang="css">
  .author-name {
    font-weight: bold;
    color: #DC3545;
  }

  .question-link {
    font-weight: bold;
    color: black;
  }

  .question-link:hover {
    color: #343A40;
    text-decoration: none;
  }
</style>
