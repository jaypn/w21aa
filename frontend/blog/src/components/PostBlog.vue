<template>
  <div>
    <p>content</p>
    <input v-model="blog_post_content" type="text" />
    <button @click="postBlog">Post</button>
  </div>
</template>

<script>
import axios from "axios";
import cookies from "vue-cookie";

export default {
  data() {
    return {
      blog_post_content: ""
    };
  },
  methods: {
    postBlog: function() {
      axios
        .request({
          url: "http://jayblogpost.ml/api/blog",
          method: "POST",
          headers: {
            "content-type": "application/json"
          },
          data: {
            content: this.blog_post_content,
            blogger_id: cookies.get("blogger_id"),
            id: this.blog_post_id
          }
        })
        .then(response => {
          console.log(response);
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style lang="scss" scoped>
</style>