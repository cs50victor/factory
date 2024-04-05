// rustimport:pyo3

use pyo3::prelude::*;

#[pyfunction]
fn say_hello() {
    println!("Hello from example, implemented in Rust!")
}

// Uncomment the below to implement custom pyo3 binding code. Otherwise, 
// rustimport will generate it for you for all functions annotated with
// #[pyfunction] and all structs annotated with #[pyclass].
//
//#[pymodule]
//fn example(_py: Python, m: &PyModule) -> PyResult<()> {
//    m.add_function(wrap_pyfunction!(say_hello, m)?)?;
//    Ok(())
//}
