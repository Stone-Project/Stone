// stone:job stone:math.double
// stone:function double_rs

#[no_mangle]
pub extern "C" fn double_rs(x: f64) -> f64 {
    x * 2.0
}
