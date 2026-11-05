// stone:job stone:math.degrees
// stone:function degrees_rs

#[no_mangle]
pub extern "C" fn degrees_rs(r: f64) -> f64 {
    r.to_degrees()
}
