// stone:job stone:math.step
// stone:function step_rs

#[no_mangle]
pub extern "C" fn step_rs(edge: f64, x: f64) -> f64 { if x < edge { 0.0 } else { 1.0 } }
