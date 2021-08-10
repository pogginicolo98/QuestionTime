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
      questions: []
    };
  },
  methods: {
    getQuestions() {
      let endpoint = "/api/questions/";
      apiService(endpoint)
        .then(data => {
          this.questions.push(...data.results);
        });
    }
  },
  created() {
    this.getQuestions();
    document.title = "QestionTime";
  }
};
</script>

<style lang="css" scoped>
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
