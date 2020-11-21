<template>
  <div>
    <post-blog />
    <h1 @click="seeBlogs()">see blogs</h1>
    <div v-for="blog in blogs" :key="blog[1]">
      <p>{{blog[2]}}</p>
      <div>
        <update-blog :blog_id="blog[1]" />
        <delete-blog :blog_id="blog[1]" />
      </div>
    </div>
  </div>
</template>

<script>
import UpdateBlog from "./UpdateBlog.vue";
import DeleteBlog from "./DeleteBlog.vue";
import PostBlog from "./PostBlog.vue";
import axios from "axios";

export default {
  components: {
    UpdateBlog,
    DeleteBlog,
    PostBlog
  },

  data() {
    return {
      blogs: []
    };
  },
  methods: {
    seeBlogs: function() {
      axios
        .request({
          url: "http://127.0.0.1:5000/blog",
          method: "GET"
        })
        .then(response => {
          console.log(response);
          this.blogs = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style scoped>