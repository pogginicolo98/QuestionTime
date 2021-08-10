<template lang="html">
  <nav class="navbar navbar-expand-lg navbar-light bg-light my-navbar">
    <div class="container">
      <!-- Brand -->
      <router-link
        :to="{ name: 'home' }"
        class="navbar-brand"
        ><img src="../../../static-storage/questiontime-96px.png"
             width="30"
             height="30"
             class="d-inline-block align-top"
             alt="Logo">
        QuestionTime
      </router-link>

      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <router-link
              :to="{ name: 'home' }"
              class="btn btn-sm btn-success mr-1"
              >Home
            </router-link>
          </li>
          <li class="nav-item">
            <router-link
              :to="{ name: 'question-editor' }"
              class="btn btn-sm btn-danger mr-1"
              >Answer
            </router-link>
          </li>
          <li class="nav-item">
            <a
              href="/accounts/logout/"
              class="btn btn-sm btn-outline-secondary"
              >Log Out
            </a>
          </li>
        </ul>
      </div>
    </div> <!-- Container -->
  </nav>
</template>

<script>
export default {
  name: "NavbarComponent",
}
</script>

<style lang="css" scoped>
  .my-navbar {
    border-bottom: 1px solid #DDD;
  }

  .navbar-brand {
    font-weight: bold;
    font-size: 130%;
  }

  .navbar-brand:hover {
    color: #DC3545 !important;
  }
</style>
