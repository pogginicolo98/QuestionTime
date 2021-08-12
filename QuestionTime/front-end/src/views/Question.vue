<template lang="html">
  <div class="single-question mt-2">
    <div class="container">
      <h1>{{ question.content }}</h1>
      <QuestionActionsComponent
        v-if="isOwner"
        :slug="slug"
      />
      <p class="mb-0">
        Question written by:
        <span class="author-name">{{ question.author }}</span>
      </p>
      <p>{{ question.created_at }}</p>
      <hr>
      <template v-if="userHasAnswered">
        <p class="answer-added">You have already answered this question.</p>
      </template>
      <template v-else-if="showForm">
        <form class="card" @submit.prevent="onSubmit">
          <div class="card-header px-3">
            Write your answer
          </div>
          <div class="card-block">
            <textarea
              v-model="newAnswerBody"
              class="form-control"
              rows="5"
              placeholder="Write your answer...">
            </textarea>
          </div>
          <div class="card-footer px-3">
            <button type="submit" class="btn btn-sm btn-success">Answer</button>
          </div>
        </form>
        <p class="text-danger mt-2">{{ error }}</p>
      </template>
      <template v-else>
        <button
          class="btn btn-sm btn-success"
          @click="showForm = true">
          Answer
        </button>
      </template>
      <hr>
      <AnswerComponent
        v-for="(answer, index) in answers"
        :answer="answer"
        :requestUser="requestUser"
        :key="index"
        @delete-answer="deleteAnswer"
      />
      <div class="my-4 text-center" >
        <div v-show="loadingAnswers">
          <div class="spinner-border text-danger mt-3"
               style="width: 3rem; height: 3rem;"
               role="status">
          </div>
        </div>
        <button
          v-show="next"
          @click="getQuestionAnswers"
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
import AnswerComponent from "@/components/Answer.vue";
import QuestionActionsComponent from "@/components/QuestionActions.vue";

export default {
  name: 'Question',
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  components: {
    AnswerComponent,
    QuestionActionsComponent
  },
  data() {
    return {
      question: {},
      answers: [],
      loadingAnswers: false,
      userHasAnswered: false,
      showForm: false,
      newAnswerBody: null,
      error: null,
      next: null,
      requestUser: null
    };
  },
  computed: {
    isOwner() {
      return this.question.author === this.requestUser;
    }
  },
  methods: {
    setPageTitle(title) {
      document.title = title;
    },
    setRequestUser() {
      this.requestUser = window.localStorage.getItem("username");
    },
    getQuestionData() {
      let endpoint = `/api/questions/${this.slug}/`
      apiService(endpoint)
        .then(questionData => {
          this.question = questionData;
          this.userHasAnswered = questionData.user_has_answered;
          this.setPageTitle(questionData.content);
        });
    },
    getQuestionAnswers() {
      let endpoint = `/api/questions/${this.slug}/answers/`;
      if (this.next) {
        endpoint = this.next;
      }
      this.loadingAnswers = true;
      apiService(endpoint)
        .then(answersData => {
          this.answers.push(...answersData.results);
          this.loadingAnswers = false;
          if (answersData.next) {
            this.next = answersData.next;
          } else {
            this.next = null;
          }
        });
    },
    onSubmit() {
      if (this.newAnswerBody) {
        let endpoint = `/api/questions/${this.slug}/answer/`;
        let method = "POST";
        let data = { body: this.newAnswerBody };
        apiService(endpoint, method, data)
          .then(answerData => {
            this.answers.push(answerData);
          });
        this.newAnswerBody = null;
        this.showForm = false;
        this.userHasAnswered = true;
        if (this.error) {
          this.error = null;
        }
      } else {
        this.error = "The answer cannot be empty.";
      }
    },
    async deleteAnswer(answer) {
      let endpoint = `/api/answers/${answer.id}/`;
      let method = "DELETE";
      try {
        await apiService(endpoint, method)
        this.answers.splice(this.answers.indexOf(answer), 1);
        this.userHasAnswered = false;
      }
      catch (err) {
        console.log(err);
      }
    }
  },
  created() {
    this.getQuestionData();
    this.getQuestionAnswers();
    this.setRequestUser();
  }
}
</script>

<style lang="css" scoped>
  .answer-added {
    color: green;
    font-weight: bold;
  }
</style>
