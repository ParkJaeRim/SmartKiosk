<template>
  <div style ="text-align: center; " class="p-3 mx-auto">
    <video  id="video" width="800" height="600" autoplay></video>
    <canvas
      id="canvas"
      width="480"
      height="360"
      style="display: none;"
    ></canvas><br>
    <!-- <b-btn @click="start">카메라 켜기</b-btn> -->
    <button style =" width: 200px; height: 120px; font-size: 80px; margin-left : 10px" @click="snap">촬영</button>
  </div>
</template>

<script>
import axios from "axios";
import constants from "../../lib/constants";
const baseURL = constants.baseUrl;
export default {
  name: "FaceCheck",
  data: () => {
    return {
      imagebase64: [],
      howmany: 5,
    };
  },
  mounted() {
       this.start();
  },
  methods: {
    start() {
      var video = document.getElementById("video");
      if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices
          .getUserMedia({ video: true })
          .then(function(stream) {
            video.srcObject = stream;
            video.play();
          });
      }
    },

    tmp(cnt) {
      var canvas = document.getElementById("canvas");
      var context = canvas.getContext("2d");
      context.drawImage(video, 0, 0, 480, 360);
      var dataURL = canvas.toDataURL();
      var x = this;

      this.imagebase64.push(dataURL);
      setTimeout(() => {
        if (cnt == this.howmany - 1) {
          // console.log(this.imagebase64);
          axios
            .post(baseURL + "/decoding", this.imagebase64)
            .then((response) => {
              this.imagebase64 = [];
              axios
                .post(baseURL + "/kiosk/recog")
                .then((response) => {
                    if(response.data.data =="찾을 수 없는 유저입니다."){
                      alert('얼굴인식 실패!')
                    }
                    x.$router.push('main')     
                })
                .catch((err) => {
                  console.log(err);
                });
            })
            .catch((err) => {
              console.log(err);
            });
        }
      }, 500);
      
    },

    snap() {
      for (let i = 0; i < this.howmany; i++) {
        this.tmp(i);
      }
    },
  },
};
</script>

<style scoped>
.cover-container {
  margin: 300px auto;
  background-color: rgba(0, 0, 0, 0.7);
  border-right: solid 3px black;
  border-bottom: solid 3px black;
}
span {
  margin: 0 auto;
}

.bcenter {
  width: 50%;
  margin: 0 auto;
}
</style>
