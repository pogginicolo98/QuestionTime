<template lang="html">
  <div class="question-actions">
    <router-link
      :to="{ name: 'question-editor', params: { slug: slug } }"
      class="btn btn-sm btn-outline-secondary mr-1"
      ><span>Edit</span>
    </router-link>
    <button
      class="btn btn-sm btn-outline-danger"
      @click="deleteQuestion"
      >Delete
    </button>
  </div>
</template>

<script>
// @ is an alias to /src
import { apiService } from "@/common/api.service.js";

export default {
  name: "QuestionActionsComponent",
  props: {
    slug: {
      type: String,
      required: true
    }
  },
  methods: {
    async deleteQuestion() {
      let endpoint = `/api/questions/${this.slug}/`;
      let method = "DELETE";
      try {
        await apiService(endpoint, method);
        this.$router.push("/");
      } catch(err) {
        console.log(err);
      }
    }
  }
}
</script>

<style lang="css" scoped>
</style>
