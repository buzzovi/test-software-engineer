import React, { useState, useEffect } from 'react';
import './App.css';
import { useForm } from "react-hook-form";
import FileBase64 from 'react-file-base64';

function PostCreate(props){
  const onPost = props.onPost
  const { handleSubmit, register, errors, reset } = useForm();
  const onFileUpload = props.onFileUpload
  let img = ""
  if (props.imgSrc.files.length>0) {
    img = <img className="displayImg" alt="img" src={props.imgSrc.files[0].base64} />
  }
  return(
    <div className="App-body">
      <form onSubmit={handleSubmit((values)=>{onPost(values,reset)})}>
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
  let img = ""
  if (props.image !== "" && props.image !== "null" ) {
    img = <img className="displayImg" alt="img" src={props.image} />
  }
  return (
  <div className="post">
    <div className="postheader">
      <span className="postusername">{props.username}</span>
      <span className="postdatetime">{props.timestamp}</span>
      <button onClick={()=>{ props.onDelPost(props.id) }} className="BlueBtn">X</button>
    </div>
    <div className="postcontent">{props.content}</div>
    { img }
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
        <button onClick={()=>{ props.onDelComment(props.postid,props.username,props.timestamp) }} className="BlueBtn">X</button>
      </div>
      <div className="postcontent">{props.comment}</div>
      <hr />
  </div>
  )
}

function CommenList(props){
  let { handleSubmit : handleSubmit2, register: register2, errors:errors2, reset:reset2 } = useForm();
  const onComment = props.onComment
  const onDelComment = props.onDelComment
  return(<div className="commenlist">
    {props.comments.map(comment => {
      return(
        <Comment key={comment.timestamp+'-'+comment.username} {...comment} postid={props.postid} onDelComment={onDelComment} />
      )})
    }
    <form onSubmit={handleSubmit2((values)=>{onComment(values,reset2)})}>
      <div className="Comment_form">
        <input type="hidden" name="postid" value={props.postid} ref={register2({})} />
        <input placeholder="User name" name="username" ref={register2({required: 'Required'})} />
          {errors2.username && 'User name is required'}
        <input placeholder="Comment" name="comment" ref={register2({required: 'Required'})} />
          {errors2.comment && 'comment is required'}
        <button className="BlueBtn">Comment!</button>
      </div>
    </form>

  </div>)
  
}

function PostList(props){
  let comments = props.posts.Items
  const onComment = props.onComment
  const onDelComment = props.onDelComment

  return(
  <div className="postlist">
    { comments.map( post =>{
      return(
        <div key={post.id}>
          <Post {...post} onDelPost={props.onDelPost}/>
          <CommenList comments={post.comments} postid={post.id} onComment={onComment} onDelComment={onDelComment} />
        </div>
      )
    })}
  </div>
  )
}

function App() {
  const [ img, setImg ] = useState({files: []})
  const [ allPost, setAllPosts ] = useState({Items: []})

  const onFileUpload = imgs =>{
    setImg({ files: [imgs] })
  }
  const onPost = (values, reset) => {
    // Create Post
    if (img.files.length>0)
      values.image = img.files[0].base64;
      
    fetch('https://bmpi7pfcqk.execute-api.eu-west-1.amazonaws.com/Prod/postcreate', {
        method: 'POST',
        body: JSON.stringify(values)
    }).then(async response => {
          const data = await response.json();
          console.log(data)
          // check for error response
          if (!response.ok) {
              // get error message from body or default to response status
              const error = (data && data.message) || response.status;
              return Promise.reject(error);
          }
          let newallPost = {...allPost}
          newallPost['Items'].push(data)
          setAllPosts(newallPost)
          reset()
      })
      .catch(error => {
          // this.setState({ errorMessage: error });
          console.error('There was an error!', error);
      });
  };

  const onComment = (values, reset2) => {
    // Create Comment
    console.log(values)
    fetch('https://bmpi7pfcqk.execute-api.eu-west-1.amazonaws.com/Prod/commentcreate', {
        method: 'POST',
        body: JSON.stringify(values)
    }).then(async response => {
          const data = await response.json();
          console.log(data)
          // check for error response
          if (!response.ok) {
              // get error message from body or default to response status
              const error = (data && data.message) || response.status;
              return Promise.reject(error);
          }
          
          let newallPost = {...allPost}
          var foundIndex = newallPost['Items'].findIndex(post => post.id === data.id);
          newallPost['Items'][foundIndex] = data;
          setAllPosts(newallPost)
          reset2()
      })
      .catch(error => {
          // this.setState({ errorMessage: error });
          console.error('There was an error!', error);
      });
  };

  const onDelComment = (id,username,timestamp) => {
    // Create Comment
    let values = {"id":id, "username": username, "timestamp": timestamp}
    console.log(values)
    fetch('https://bmpi7pfcqk.execute-api.eu-west-1.amazonaws.com/Prod/commentdelete', {
        method: 'POST',
        body: JSON.stringify(values)
    }).then(async response => {
          const data = await response.json();
          console.log(data)
          // check for error response
          if (!response.ok) {
              // get error message from body or default to response status
              const error = (data && data.message) || response.status;
              return Promise.reject(error);
          }
          
          let newallPost = {...allPost}
          var foundIndex = newallPost['Items'].findIndex(post => post.id === data.id);
          newallPost['Items'][foundIndex] = data;
          setAllPosts(newallPost)
      })
      .catch(error => {
          // this.setState({ errorMessage: error });
          console.error('There was an error!', error);
      });
  };
  const onDelPost = id => {
    // Delete Post
    fetch('https://bmpi7pfcqk.execute-api.eu-west-1.amazonaws.com/Prod/postdelete', {
        method: 'POST',
        body: JSON.stringify({"id":id})
    }).then(async response => {
          const data = await response.json();
          console.log(data)
          // check for error response
          if (!response.ok) {
              // get error message from body or default to response status
              const error = (data && data.message) || response.status;
              return Promise.reject(error);
          }
          let newallPost = {...allPost}
          newallPost['Items'] = newallPost['Items'].filter((post)=>{return post.id !== data.id })
          setAllPosts(newallPost)
      })
      .catch(error => {
          // this.setState({ errorMessage: error });
          console.error('There was an error!', error);
      });
  };

    
  useEffect(() => {
    // GetPostsList
    fetch("https://bmpi7pfcqk.execute-api.eu-west-1.amazonaws.com/Prod/postlist")
        .then(res => res.json())
        .then(
          (result) => {
            setAllPosts(result);
          },
          (error) => {
            console.log("Error")
          }
        )
  }, [])
  
  return (
    <div className="App">
      <PostCreate onPost={onPost} onFileUpload={onFileUpload} imgSrc={img}  />
      <PostList posts={allPost} onDelPost={onDelPost} onComment={onComment} onDelComment={onDelComment}   />
    </div>
  );
}

export default App;
