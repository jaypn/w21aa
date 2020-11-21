<template>
  <div>
    <p>blog content</p>
    <input v-model="blog_postContent" type="text" />
    <button @click="updateBlog">update</button>
  </div>
</template>

<script>
import axios from "axios";
import cookies from "vue-cookie";
export default {
  name: "update-blog",
  data() {
    return {
      blog_postContent: ""
    };
  },
  props: {
    blog_id: {
      type: Number,
      required: true
    }
  },
  methods: {
    updateBlog: function() {
      axios
        .request({
          url: "http://127.0.0.1:5000/blog",
          method: "PATCH",
          headers: {
            "content-type": "application/json"
          },
          data: {
            content: this.blog_postContent,

            blogger_id: cookies.get("blogger_id"),
            id: this.blog_id
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