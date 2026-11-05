// stone:job stone:math.cube
// stone:function cube_rs

#[no_mangle]
pub extern "C" fn cube_rs(x: f64) -> f64 {
    x * x * x
}
