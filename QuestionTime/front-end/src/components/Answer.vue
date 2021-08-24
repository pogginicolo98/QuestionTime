<template lang="html">
  <div class="single-answer">
    <p class="text-muted">
      <strong>{{ answer.author }}</strong> answered on {{ answer.created_at }}
    </p>
    <p>{{ answer.body }}</p>
    <div v-if="isAnswerAuthor" class="answer-owner">
      <router-link
        :to="{ name: 'answer-editor', params: { id: answer.id } }"
        class="btn btn-sm btn-outline-secondary mr-1">
        <span>Edit</span>
      </router-link>
      <button
        class="btn btn-sm btn-outline-danger"
        @click="triggerDeleteAnswer">
        Delete
      </button>
    </div>
    <div v-else
         class="like-answer">
      <button
        class="btn btn-sm"
        :class="{
            'btn-danger': userLikedAnswer,
            'btn-outline-danger': !userLikedAnswer
          }"
        @click="toggleLike">
        <strong>Like [{{ likesNumber }}]</strong>
      </button>
    </div>
    <hr>
  </div>
</template>

<script>
// @ is an alias to /src
import { apiService } from "@/common/api.service.js";

export default {
  name: "AnswerComponent",
  props: {
    answer: {
      type: Object,
      required: true
    },
    requestUser: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      userLikedAnswer: this.answer.user_has_voted,
      likesNumber: this.answer.likes_count
    }
  },
  computed: {
    isAnswerAuthor() {
      return this.answer.author === this.requestUser;
    }
  },
  methods: {
    triggerDeleteAnswer() {
      this.$emit("delete-answer", this.answer);
    },
    likeAnswer() {
      this.userLikedAnswer = true;
      this.likesNumber += 1;
      let endpoint = `/api/answers/${this.answer.id}/like/`;
      let method = "POST";
      apiService(endpoint, method);
    },
    unlikeAnswer() {
      this.userLikedAnswer = false;
      this.likesNumber -= 1;
      let endpoint = `/api/answers/${this.answer.id}/like/`;
      let method = "DELETE";
      apiService(endpoint, method);
    },
    toggleLike() {
      this.userLikedAnswer === false
        ? this.likeAnswer()
        : this.unlikeAnswer()
    }
  }
}
</script>

<style lang="css" scoped>
</style>
