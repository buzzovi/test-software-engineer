import React, { useState } from 'react';
import allpost from './all.json';
import './App.css';
import { useForm } from "react-hook-form";
import FileBase64 from 'react-file-base64';


function PostCreate(props){
  const onSubmit = props.onSubmit
  const handleSubmit = props.handleSubmit
  const register = props.register
  const errors = props.errors
  const onFileUpload = props.onFileUpload
  let img = ""
  if (props.imgSrc.files.length>0) {
    img = <img className="displayImg" alt="img" src={props.imgSrc.files[0].base64} />
  }
  return(
    <div className="App-body">
      <form onSubmit={handleSubmit(onSubmit)}>
        <h1>The Keisen Blog</h1>
        <div className="Post_form">
          <input name="username" ref={register({ required: 'Required'})} placeholder="User name" />
          {errors.username && 'User name is required'}
          <textarea name="content" 
            ref={register({
              required: 'Required'
            })} 
            placeholder="Post content" />
          {errors.content && 'Post content is required'}
          <FileBase64 className="uploadImg"
            multiple={ false }
            onDone={ onFileUpload } />
            { img }
        </div>
        <button type="submit" className="BlueBtn">Post!</button>
      </form>
    </div>
  )
}

function Post(props){
  return (
  <div className="post">
    <div className="postheader">
      <span className="postusername">{props.username}</span>
      <span className="postdatetime">{props.timestamp}</span>
    </div>
    <div className="postcontent">{props.content}</div>
    <hr />
  </div>
  )
}

function Comment(props){
  return (
    <div className="post">
      <div className="postheader">
        <span className="postusername">{props.username}</span>
        <span className="postdatetime">{props.timestamp}</span>
        <span className="postdelete">D</span>
      </div>
      <div className="postcontent">{props.comment}</div>
      <hr />
  </div>
  )
}

function CommenList(props){
  return(<div className="commenlist">
    {props.comments.map(comment => {
      return(
        <Comment key={comment.timestamp+'-'+comment.username} {...comment} />
      )})
    }
    <div className="Comment_form">
      <input placeholder="User name" />
      <input placeholder="Comment" />
      <button className="BlueBtn">Comment!</button>
    </div>

  </div>)
  
}

function PostList(props){
  let comments = props.posts.Items

  return(
  <div className="postlist">
    { comments.map( post =>{
      return(
        <div key={post.id}>
          <Post {...post}/>
          <CommenList comments={post.comments} />
        </div>
      )
    })}
  </div>
  )
}

function App() {
  const { handleSubmit, register, errors } = useForm();
  const [ img, setImg ] = useState({files: []})

  const onFileUpload = imgs =>{
    setImg({ files: [imgs] })
  }
  const onSubmit = values => {
    if (img.files.length>0)
      values.images = img.files[0].base64;
    console.log(values);
  };


  return (
    <div className="App">
      <PostCreate onSubmit={onSubmit} handleSubmit={handleSubmit} register={register} errors={errors} onFileUpload={onFileUpload} imgSrc={img} />
      <PostList posts={allpost}  />
    </div>
  );
}

export default App;
