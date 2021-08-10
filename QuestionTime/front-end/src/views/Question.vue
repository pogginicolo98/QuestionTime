<template lang="html">
  <div class="single-question mt-2">
    <div class="container">
      <h1>{{ question.content }}</h1>
      <p class="mb-0">
        Question written by:
        <span class="author-name">{{ question.author }}</span>
      </p>
      <p>{{ question.created_at }}</p>
      <hr>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { apiService } from "@/common/api.service.js";

export default {
  name: 'Question',
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      question: {}
    };
  },
  methods: {
    setPageTitle(title) {
      document.title = title;
    },
    getQuestionData() {
      let endpoint = `/api/questions/${this.slug}/`
      apiService(endpoint)
        .then(data => {
          this.question = data;
          this.setPageTitle(data.content);
        });
    }
  },
  created() {
    this.getQuestionData();
  }
}
</script>

<style lang="css" scoped>
</style>
