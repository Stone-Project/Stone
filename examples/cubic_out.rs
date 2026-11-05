// stone:job stone:math.cubic_out
// stone:function cubic_out_rs

#[no_mangle]
pub extern "C" fn cubic_out_rs(t: f64) -> f64 {
    let u = 1.0 - t;
    1.0 - u * u * u
}
