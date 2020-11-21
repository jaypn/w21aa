<template>
  <div>
    <button @click="deleteBlog()">delete</button>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "delete-blog",

  props: {
    blog_id: {
      type: Number,
      required: true
    }
  },
  methods: {
    deleteBlog: function() {
      axios
        .request({
          url: "http://jayblogpost.ml/api/blog",
          method: "DELETE",
          headers: {
            "content-type": "application/json"
          },
          data: {
            blog_id: this.blog_id
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