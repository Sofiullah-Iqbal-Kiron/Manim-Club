function CountQuiz(props) {
  const [state, setState] = useState({ num1: 0, num2: 0, sum: "" });

  useEffect(() => {
    document.title = "hello";
  });

  return (
    <>
      <h1>
        {state.num1} + {state.num2} ?
      </h1>
      <input className="inField" value="" />
    </>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<CountQuiz />);