import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(page_title="Voice to Text", layout="centered")
st.title("🎤 Voice to Text App")
st.markdown("Click the mic button, speak something, and get the transcript in real-time!")

# JavaScript + HTML to record audio and send to backend later
record_audio_html = """
<div style="text-align: center;">
  <button onclick="startRecording()" style="padding: 10px 20px; font-size: 18px;">🎙️ Start Speaking</button>
  <p id="status" style="margin-top: 10px;">Status: Idle</p>
</div>

<script>
let mediaRecorder;
let audioChunks = [];

function startRecording() {
  navigator.mediaDevices.getUserMedia({ audio: true })
    .then(stream => {
      document.getElementById("status").innerText = "Status: Recording...";
      mediaRecorder = new MediaRecorder(stream);
      mediaRecorder.start();

      mediaRecorder.ondataavailable = event => {
        audioChunks.push(event.data);
      };

      mediaRecorder.onstop = () => {
        const audioBlob = new Blob(audioChunks);
        const reader = new FileReader();
        reader.readAsDataURL(audioBlob);
        reader.onloadend = function () {
          const base64data = reader.result.split(',')[1];
          const input = document.createElement("input");
          input.type = "hidden";
          input.name = "audio";
          input.value = base64data;
          document.body.appendChild(input);
        };
      };

      setTimeout(() => {
        mediaRecorder.stop();
        document.getElementById("status").innerText = "Status: Done Recording";
      }, 4000); // 4 seconds max
    });
}
</script>
"""

components.html(record_audio_html, height=180)

# Simulated Transcription (replace this with actual model integration)
if st.button("🧠 Generate Transcription"):
    with st.spinner("Transcribing..."):
        st.success("Transcription complete ✅")
        st.markdown("**You said:** Hello, this is a test voice transcription.")
        st.markdown("_(Note: This is placeholder text. Real transcription will be added soon.)_")


