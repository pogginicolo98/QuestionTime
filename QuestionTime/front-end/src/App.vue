<template>
  <div id="app">
    <NavbarComponent />
    <router-view />
  </div>
</template>

<script>
  import NavbarComponent from "./components/Navbar.vue";
  import { apiService } from "./common/api.service.js";

  export default {
    name: "App",
    components: {
      NavbarComponent
    },
    data() {
      return {
        userUsername: null
      }
    },
    methods: {
      async setUserInfo() {
        let endpoint = "/api/user/";
        await apiService(endpoint)
                .then(user_data => {
                  this.userUsername = user_data.username;
                  window.localStorage.setItem("username", this.userUsername);
                });
      }
    },
    created() {
      this.setUserInfo();
    }
  }
</script>

<style>
  body {
    font-family: 'Playfair Display', serif;
  }

  .btn:focus {
    box-shadow: none !important;
  }
</style>
